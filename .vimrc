" Install vim-plug 
let need_to_install_plugins = 0
if empty(glob('~/.vim/autoload/plug.vim'))
    silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    "autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
    let need_to_install_plugins = 1
endif

" Plugins
call plug#begin()
Plug 'altercation/vim-colors-solarized'
Plug 'ycm-core/YouCompleteMe', { 'do': './install.py'}
call plug#end()

if need_to_install_plugins == 1
    echo "Installing plugins..."
    silent! PlugInstall
    echo "Done!"
    q
endif

" Display Line Numbers
set number

" Solarized Theme
syntax enable
set background=dark
colorscheme solarized

" Allow saving files as sudo when I forgot to start vim using sudo
cmap w!! w !sudo tee > /dev/null %

" YCM autocompletion
" Auto close preview window
let g:ycm_autoclose_preview_window_after_completion=1
" Fix for interpreter
let g:ycm_server_python_interpreter = '/usr/bin/python3.8'

