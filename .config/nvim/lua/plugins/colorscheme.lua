return {
    'maxmx03/solarized.nvim',
    lazy = false,
    priority = 1000,
    ---@type solarized.config
    opts = {
        variant = "spring",
        plugins = {
            treesitter = true,
        },
    },
    config = function(_, opts)
        vim.o.termguicolors = true
        vim.o.background = 'dark'
        require('solarized').setup(opts)
        vim.cmd.colorscheme 'solarized'
    end,
}
