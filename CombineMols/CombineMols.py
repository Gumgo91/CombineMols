from rdkit import Chem
from rdkit import RDLogger
from mendeleev import element

RDLogger.DisableLog('rdApp.*')  # for skip RDKit messages


def CombineMols(mol1, mol2, dummy=53, bridge=0):
    """
    CombineMols( (Mol/str)mol1, (Mol/str)mol2, (int,str)dummy) -> list:
        Returns list of possible combinations of combined molecules
            Arguments:
                - mol1: (Mol/SMILES string) the molecule 
                - mol2: (Mol/SMILES string) the molecule 
                - dummy: (int of atomic num/str of atomic symbol) The atomic number or symbol of the dummy atom, which
                indicates the atom you want to bond with.
                - bridge: (int of atomic num/str of atomic symbol) Before intermolecular connections, add bridge atoms
            Returns:
                Mol
    """
    if type(dummy) == str:
        # If the dummy atom is given an atomic symbol, replace it with an atomic number
        dummy = element(dummy).atomic_number
        
    if type(bridge) == str:
        bridge = element(bridge).atomic_number         

    # Convert to molecule class if given SMILES string type
    if type(mol1) == str:
        mol1 = Chem.MolFromSmiles(mol1)

    if type(mol2) == str:
        mol2 = Chem.MolFromSmiles(mol2)
    
    #If a bridge atom is given, the dummy atoms are extended in batches
    if bridge !=0 :
        mol1 = Chem.ReplaceSubstructs(mol1,
                                     Chem.MolFromSmiles(element(dummy).symbol),
                                     Chem.MolFromSmiles('{}{}'.format(element(dummy).symbol,element(bridge).symbol)),
                                     replaceAll=True,
                                     replacementConnectionPoint=1)[0]
    
    bonds = list()
    for atom in mol1.GetAtoms():
        if atom.GetAtomicNum() == dummy:
            bond = atom.GetBonds()[0]  # (dummy atom, the atom connected to dummy atom)
            bonds.append((atom.GetIdx(),
                          bond.GetBeginAtomIdx() if atom.GetIdx() != bond.GetBeginAtomIdx() else bond.GetEndAtomIdx()))

    molecules = list()
    for bond in bonds:
        # Remove dummy atom
        oriAtom = mol1.GetAtoms()[bond[1]].GetAtomicNum()  # Save the atomic number of the original atom
        mol1e = Chem.EditableMol(mol1)
        # Replace dummy atom with [Po] so that the atom connected to dummy atom have the highest priority.
        Chem.rdchem.EditableMol.ReplaceAtom(mol1e, bond[1], Chem.Atom(84))
        Chem.rdchem.EditableMol.RemoveAtom(mol1e, bond[0])
        new_mol = mol1e.GetMol()
        
        
        for j, atom in enumerate(new_mol.GetAtoms()):
            if atom.GetAtomicNum() == 84:
                atom_index = j
                break
        
        
        mod_mol = Chem.ReplaceSubstructs(mol2,
                                         Chem.MolFromSmiles(element(dummy).symbol),
                                         new_mol,
                                         replaceAll=False,
                                         replacementConnectionPoint=j)

        for i in range(len(mod_mol)):
            for j, atom in enumerate(mod_mol[i].GetAtoms()):
                if atom.GetAtomicNum() == 84:
                    mod_mol[i].GetAtoms()[j].SetAtomicNum(oriAtom)
                    break
        for img_mol in mod_mol:
            try:
                Chem.Draw.MolToImage(img_mol)  # skip wrong molecules
                molecules.append(img_mol)
            except:
                pass
    return molecules