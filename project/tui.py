from rich.console import Console
from rich.json import JSON
from rich import spinner
console = Console()

from prompt_toolkit.shortcuts import radiolist_dialog

result = radiolist_dialog(
    title="RadioList dialog",
    text="Which breakfast would you like ?",
    values=[
        ("breakfast1", "Eggs and beacon"),
        ("breakfast2", "French breakfast"),
        ("breakfast3", "Equestrian breakfast")
    ]
).run()

from prompt_toolkit.shortcuts import checkboxlist_dialog

results_array = checkboxlist_dialog(
    title="CheckboxList dialog",
    text="What would you like in your breakfast ?",
    values=[
        ("eggs", "Eggs"),
        ("bacon", "Bacon"),
        ("croissants", "20 Croissants"),
        ("daily", "The breakfast of the day")
    ]
).run()


from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit.styles import Style

results = checkboxlist_dialog(
    title="CheckboxList dialog",
    text="What would you like in your breakfast ?",
    values=[
        ("eggs", "Eggs"),
        ("bacon", "Bacon"),
        ("croissants", "20 Croissants"),
        ("daily", "The breakfast of the day")
    ],
    style=Style.from_dict({
        'dialog': 'bg:#cdbbb3',
        'button': 'bg:#bf99a4',
        'checkbox': '#e8612c',
        'dialog.body': 'bg:#a9cfd0',
        'dialog shadow': 'bg:#c98982',
        'frame.label': '#fcaca3',
        'dialog.body label': '#fd8bb6',
    })
).run()
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("white on blue", style="white on blue")
console.log("Hello, World!")
console.print_json('[false, true, null, "foo"]')
console.rule("[bold red]Chapter 2")

console.log(JSON('["foo", "bar"]'))
with console.status("Working..."):
    print('Finished working')

with console.status("Monkeying around...", spinner="monkey"):
    spinner
    input()
    print('Finished working')
    
