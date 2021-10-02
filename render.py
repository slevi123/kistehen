from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from sample_data.parties import parties

def render():
    # pure_path = Path.cwd() / "sites"

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )

    # register_filters(env)

    def process(file_name, context={}, template_path=None):
        if not template_path:
            template_path = file_name

        pure_path = ""
        for _ in range(file_name.count("/")):
            pure_path += "../"
        if not pure_path:
            pure_path = "./"
        pure_path = pure_path[:-1]
        site = env.get_template(template_path).render(pure_path=pure_path, **context)
        (Path(f"./docs")/file_name).write_text(site, encoding='utf-8')    # sites

    process("index.html")

    process("parties.html", context={"parties": parties})
    process("res/css/base.css", template_path="css/base.css", )

if __name__ == "__main__":
    render()