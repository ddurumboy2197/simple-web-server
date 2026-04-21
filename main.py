import argparse

class CLIApp:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Mini CLI Framework')

    def add_command(self, name, func):
        subparser = self.parser.add_subparsers(dest='command')
        subparser.required = True
        subparser.add_parser(name).set_defaults(func=func)

    def run(self):
        args = self.parser.parse_args()
        if hasattr(args, 'func'):
            args.func(args)

def main():
    app = CLIApp()

    @app.add_command('hello')
    def hello(args):
        print('Hello, world!')

    @app.add_command('add')
    def add(args):
        if len(args) != 3:
            app.parser.print_help()
            return
        a, b = map(int, args[1:])
        print(f'{a} + {b} = {a + b}')

    app.run()

if __name__ == '__main__':
    main()
```

Kodni ishga tushirish uchun quyidagicha buyruqlar yozing:

```bash
python cli_app.py hello
python cli_app.py add 2 3
python cli_app.py add
