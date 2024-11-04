vim.cmd("set expandtab")
vim.cmd("set tabstop=4")
vim.cmd("set softtabstop=4")
vim.cmd("set shiftwidth=4")

vim.opt.number = true
vim.opt.relativenumber = true

---- Key maps
-- Leader
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

-- Move through buffers
vim.keymap.set('n', '<leader><Left>', '<Cmd>bp!<CR>', { silent = true })
vim.keymap.set('n', '<leader><Right>', '<Cmd>bn!<CR>', { silent = true })
vim.keymap.set('n', '<leader>bd', '<Cmd>bd<CR>', { silent = true })

-- pretty json
vim.keymap.set('n', '<leader>jq', '<Cmd>%!jq -S<CR>', { silent = true })

require("config.lazy")
