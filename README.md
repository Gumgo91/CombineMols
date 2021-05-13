# Welcome to CombineMols

CombineMols is a python package for easily combining two molecules.

This intuitively aids in the combining of molecules using dummy atoms.

The easiest way to install the dependencies is to install the Anaconda 3 Python distribution and use conda 
to set up an environment with RDKit.

# Dependencies

rdkit / mendeleev

# Installation

## Step 1 :
Make a new conda environment and install RDKit.
```
conda create -c rdkit -n my-rdkit-env rdkit
```
Then activate this new environment.
```
conda activate my-rdkit-env
```

## Step 2 :
Inside this environment install CombineMols.

**Using pip**
```
pip install CombineMols
```

# Examples
![example](https://user-images.githubusercontent.com/65825773/118081640-baaa9400-b3f6-11eb-8416-cc19a32922a8.png)

Two molecule classes can be combined.
```
mol1 = Chem.MolFromSmiles('IOc1c[nH]c2ncc(I)cc12')
mol2 = Chem.MolFromSmiles('Sc1cccc(I)c1I')
CombineMols(mol1, mol2, "I")
```

Molecules can be entered directly in SMILES form.
```
mol1 = 'IOc1c[nH]c2ncc(I)cc12'
mol2 = 'Sc1cccc(I)c1I'
CombineMols(mol1, mol2, "I")
```

Dummy atom can be entered by atomic number.
```
mol1 = 'IOc1c[nH]c2ncc(I)cc12'
mol2 = 'Sc1cccc(I)c1I'
CombineMols(mol1, mol2, 53)
```
