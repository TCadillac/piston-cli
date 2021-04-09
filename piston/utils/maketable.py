from rich import box
from rich.table import Table


class MakeTable:
    """TODO: Write a Docstring here."""

    @staticmethod
    def mktbl(cont: list) -> Table:
        """Make a table list from rich library."""
        l_table = Table(title="Theme List", show_header=False, box=box.ROUNDED)
        l_table.add_column(justify="center", style="cyan", no_wrap=True)
        l_table.add_column(justify="center", style="magenta", no_wrap=True)

        for lang in cont:
            try:
                l_table.add_row(lang[0], lang[1])
            except IndexError:
                l_table.add_row(lang[0], "")
        return l_table


MakeTable = MakeTable()
