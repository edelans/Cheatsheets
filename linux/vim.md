# List of useful commands


## recap of different movements
    - `w` - jusqu'au début du prochain mot, en EXCLUANT son premier caractère.
    - `e` - jusqu'à la fin du mot courant, en EXCLUANT son dernier caractère.
    - `$` - jusqu'à la fin de la ligne, en INCLUANT son dernier caractère.
NB : on peut ajouter un quantificateur avant le mouvement (ex: `2w` déplace le curseur 2 mots vers l'avant).

## navigation
- h,j,k,l (j ressemble à une flèche vers le bas)
- `ctrl+G` to display position in the file, and status
- `23G` go to line # 23
- `G` go to the end of file
- `gg` go to begining of file
- `^^` go to beginning of line
- `$$` go to end of line

## search
- `*` search for the word I am currently standing on
- `/` to search for a string and then `n` or `N` to navigate between results
- `%`  pour trouver des ), ] ou } correspondants
 
## undo
- `u` undo last operation
- `U` undo all operations on this line
- `ctrl+r` to redo

## copy pasting
- `d` deletes works like cut
- `y` yank (copy)
- 'p' pastes what you have copied/deleted

## basic editing

### deletion
- `x`   pour effacer le caractère sous le curseur
- `dw` to erase a word
- `d$` to erase until end of line
- `dd` to erase the whole line
-  `ciw` : delete the word you standing on and enter insert mode

### instertion
- `i` for inserting before the cursor
- `a` for inserting after the cursor
- `A` for inserting at the end of the line
- `I' for inserting at the beginning of the line
- `o` for adding a new line below line of the cursor and enter insert mode
- `O` for adding a new line *above* the line of the cursor and enter insert mode
- `r` replaces the letter under the cursor
- `R` enter remplace mode. Like insert mode but every char you type replaces the one under your cursor 
- `c` changes (delete according to movement and enter insert mode)
- `:s/ancien/nouveau/g`  pour remplacer 'ancien' par 'nouveau'. L'ajout du drapeau  g  ordonne de faire une substitution globale sur la ligne, et change toutes les occurrences de "le" sur la ligne.


## external commands
- `ctrl-z` to background Vim, type in a few shell commands for git or whatever and then use `fg` to hop back into Vim.
- `:!`  suivi d'une commande externe pour exécuter cette commande


## visual mode
- `Shift+v` to select a block of text and do a single operation to the same portion of text on several lines (regexp, aligning, etc.)
- `ctrl-v` allows you to manipulate a block of text, or insert text on multiple lines at once using I or A for before or after the block



