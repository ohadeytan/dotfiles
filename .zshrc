# History
HISTFILE=~/.histfile
HISTSIZE=1000000000
SAVEHIST=1000000000

# Enable colors
autoload -U colors && colors

# bat as manpager 
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# Enable vim mode
bindkey -v

# Starship prompt
eval "$(starship init zsh)"
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE=\'fg=60\'

# Aliases
source ~/.config/aliases.sh

# Plugins
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
