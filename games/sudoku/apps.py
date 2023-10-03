from django.apps import AppConfig


class SudokuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sudoku'

    def ready(self):
        import sudoku.signals