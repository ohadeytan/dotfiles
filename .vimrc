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
Plug 'preservim/nerdtree'
Plug 'Glench/Vim-Jinja2-Syntax'
Plug 'junegunn/fzf.vim'
Plug 'itchyny/lightline.vim'
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

" NERDTree
let NERDTreeIgnore = ['\.pyc$', '__pycache__']
let NERDTreeMinimalUI = 1
let g:nerdtree_open = 0
map <C-n> :NERDTreeToggle<CR>

" Indentation
set shiftwidth=4 softtabstop=4 expandtab
autocmd FileType java setlocal shiftwidth=2 softtabstop=2 
autocmd FileType markdown setlocal shiftwidth=2 softtabstop=2 
set breakindent
set showbreak=↪\  

" Key maps
let mapleader = " "
" Move through buffers
nmap <leader><Left> :bp!<CR>
nmap <leader><Right> :bn!<CR>
nmap <leader>d :bd<CR>

" fzf
nnoremap <silent> <leader>f :Files<CR>
nnoremap <silent> <leader>b :Buffers<CR>
nnoremap <silent> <leader>s :Lines<CR>
nnoremap <silent> <leader>hf :History<CR>
nnoremap <silent> <leader>hv :History:<CR>

" lightline
set laststatus=2
set noshowmode
let g:lightline = {
    \ 'colorscheme': 'solarized',
    \ }
