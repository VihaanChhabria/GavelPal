def clear_all_widgets(self):
    for widget in self.root.winfo_children():
        widget.destroy()
