# History
HISTFILE=~/.histfile
HISTSIZE=1000000000
SAVEHIST=1000000000
setopt share_history

# Enable colors
autoload -U colors && colors
autoload -U compinit && compinit

# bat as manpager 
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# Enable vim mode
bindkey -v

# Starship prompt
eval "$(starship init zsh)"

# Aliases
source ~/.config/aliases.sh

# Private stuff
source ~/.config/private.sh

### Plugins
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Completion
source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#a8a8a8"
bindkey "^F" forward-word
bindkey "^B" backward-word
eval "$(_PIPENV_COMPLETE=zsh_source pipenv)"

# fzf
source /usr/share/fzf/shell/key-bindings.zsh
source /usr/share/fzf/shell/completion.zsh
source /usr/share/zsh/plugins/fzf-tab-bin-git/fzf-tab.plugin.zsh

# Use vim
export EDITOR=/usr/bin/vim
