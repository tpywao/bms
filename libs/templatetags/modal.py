from django import template
from django.template import NodeList
from django.template import TemplateSyntaxError
from hamlpy.compiler import Compiler

register = template.Library()


@register.tag('modal')
def do_modal(parser, token):
    # {% modal id %}
    args = token.split_contents()[1:]
    if len(args) != 1:
        raise TemplateSyntaxError(
            "'modal' takes 1 argument, the modal id.".format(
                token.lineno,
                token.contents
                ))
    elems = dict(id=args[0])

    # modal title
    nodelist = parser.parse((
        'modal_body',
        'modal_negative',
        'modal_positive',
        'endmodal',
        ))
    token = parser.next_token()
    elems['title'] = nodelist

    # {% modal_body %}
    if token.contents == 'modal_body':
        nodelist = parser.parse((
            'modal_negative',
            'modal_positive',
            'endmodal',
            ))
        token = parser.next_token()
        elems['body'] = nodelist

    # {% modal_negative %} (optional)
    if token.contents == 'modal_negative':
        nodelist = parser.parse((
            'modal_positive',
            'endmodal',
            ))
        token = parser.next_token()
        elems['negative'] = nodelist

    # {% modal_positive %} (optional)
    if token.contents == 'modal_positive':
        nodelist = parser.parse((
            'endmodal',
            ))
        token = parser.next_token()
        elems['positive'] = nodelist

    # {% endmodal %}
    if token.contents != 'endmodal':
        raise TemplateSyntaxError(
            'Malformed template tag at line {0}: "{1}"'.format(
                token.lineno,
                token.contents
                ))

    return ModalNode(elems)


class ModalNode(template.Node):
    modal_haml = '''
        %div.modal.fade{id: "{id}", tabindex: "-1", role: "dialog"}
            %div.modal-dialog{role: "document"}
                %div.modal-content
                    %div.modal-header
                        %button.close{
                            type: "button",
                            data-dismiss: "modal",
                            aria-label: "Close"}
                            %span{aria-hidden: "true"}
                                &times;
                        %h4.modal-title
                            {title}
                    %div.modal-body
                        {body}
        '''
    modal_footer = '''
                    %div.modal-footer
        '''
    modal_negative = '''
                        %button.btn.btn-default{
                            type: "button",
                            data-dismiss: "modal"
                            }
                            {negative}
        '''
    modal_positive = '''
                        %button.btn.btn-primary{type: "button"}
                            {positive}
        '''

    def __init__(self, elems):
        self.elems = elems
        self.haml = self.modal_haml

        has_negative = 'negative' in elems
        has_positive = 'positive' in elems
        if has_negative or has_positive:
            self.haml += self.modal_footer
            if has_negative:
                self.haml += self.modal_negative
            if has_positive:
                self.haml += self.modal_positive

    def render(self, context):
        compiler = Compiler()
        html = compiler.process(self.haml)

        modal_elements = {}
        for key, nodelist in self.elems.items():
            rendered_nodelist = ''
            if isinstance(nodelist, NodeList):
                for node in nodelist:
                    rendered_nodelist += node.render(context)
            else:
                rendered_nodelist += nodelist
            modal_elements[key] = rendered_nodelist

        return html.format(**modal_elements)
