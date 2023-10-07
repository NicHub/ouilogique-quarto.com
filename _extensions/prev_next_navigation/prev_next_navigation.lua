local function search_value (tbl, val)
    for i = 1, #tbl do
        if tbl[i] == val then
            return i
        end
    end
    return nil
end

function Pandoc(doc)
    if not doc.meta.draft then
        html_str =
        [[<!-- From prev_next_navigation.lua -->
<script src="/js/prev_next_links.js"></script>
<script src="/js/prev_next_buttons.js"></script>
]]
        quarto.doc.include_text("after-body", html_str)
    else
        quarto.log.warning("this file is a draft")
    end

    -- Other possibility:
    -- pandoc.path.split_extension(PANDOC_STATE.output_file)
    local full_path = pandoc.path.split(quarto.doc.input_file)
    local fname_with_ext = full_path[#full_path]
    local fname_wo_ext = pandoc.path.split_extension(fname_with_ext)
    quarto.log.warning(full_path)
    quarto.log.warning(fname_wo_ext)
    quarto.log.warning(type(full_path))

    if search_value(full_path, "posts") then
        quarto.log.warning("posts")
    else
        quarto.log.warning("not posts")
    end
end
