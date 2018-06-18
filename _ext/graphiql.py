import fett
from docutils import statemachine
from docutils.utils.error_reporting import ErrorString
from sphinx.util.compat import Directive


class GraphiQLDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {"query": str, "response": str}

    GRAPHIQL_TEMPLATE = '''
.. raw:: html

   <div class="graphiql">
   Loading...
   <div class="query">
   {{ query }}
   </div>
   <div class="response">
   {{ response }}
   </div>
   </div>
'''

    def run(self):
        graphiql_template = fett.Template(self.GRAPHIQL_TEMPLATE)
        try:
            rendered = graphiql_template.render(self.options)
        except Exception as error:
            raise self.severe('Failed to render template: {}'.format(ErrorString(error)))

        rendered_lines = statemachine.string2lines(rendered, 4, convert_whitespace=1)

        self.state_machine.insert_input(rendered_lines, '')

        return []


def setup(app):
    app.add_directive('graphiql', GraphiQLDirective)

    return {'parallel_read_safe': True,
            'parallel_write_safe': True}