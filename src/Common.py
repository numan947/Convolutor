def entrySelectAllHandler(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'
