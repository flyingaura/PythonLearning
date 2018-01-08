
from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_header_js(the_title, js_string):    #带JS代码的模板
    with open('templates/header_with_js.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title, script=js_string))

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, name='', form_type="POST"):
    return('<form action="' + the_url + '" name="' + name + '" method="' + form_type + '">')

def end_form(submit_msg="Submit", style = None):
    if(style):
        style_string = 'class="' + style + '"'
    else:
        style_string = ''
    return('<input type=submit value="' + submit_msg + '" ' + style_string + '></form>')

def subbutton(subvalue, suburl , style = None):
    if (style):
        style_string = 'class="' + style + '"'
    else:
        style_string = ''

    return ('<input type="button" value="' + subvalue + '" onclick="' + suburl + '" ' + style_string + '>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def create_inputs(name_string, value = None, style = None):
    if(value):
        value_string = '" value="' + value + '"'
    else:
        value_string = ''
    if(style):
        style_string = ' class="' + style + '"'
    else:
        style_string = ''

    return ('<input type="text" name="' + name_string + '"' + value_string + style_string + '>')

def checked_box(cb_name,cb_value, cb_show = None, cb_title = None, checked = False):
    if(not cb_title):
        cb_title = cb_value
    if(not cb_show):
        cb_show = cb_value
    if(checked):
        checked_string = 'checked'
    else:
        checked_string = ''
    return('<input type="checkbox" name="' + cb_name + '" value="' + cb_value + '" title="' + cb_title + '" ' + checked_string + '>' +
           '<span style="font-size:24px;color:#FF6666;font-weight:bolder;">' + cb_show + '</span>&nbsp;&nbsp;&nbsp;&nbsp;')

def select_set(selname, option_dic, size = '1', multiple = False, SelectedVals = []):
    if(multiple):
        mul_string = 'multiple'
    else:
        mul_string = ''

    Web_string = '<select name="' + selname + '" size="' + str(size) + '" ' + mul_string + '>' + '\n'
    option_string = ''
    for option in option_dic:
        if(option in SelectedVals):
            selected_string = 'selected="selected"'
        else:
            selected_string = ''
        option_string = option_string + '<option value="' + str(option) + '" ' + selected_string + '>' + str(option_dic[option]) + '</option>' + '\n'

    Web_string = Web_string + option_string + '</select>'

    return Web_string

def input_hidden(name_string,value=None):
    if(value != None):
        input_string = '<input type="hidden" name="' + name_string + '" value="' + str(value) + '">'
    else:
        input_string = '<input type="hidden" name="' + name_string + '">'

    return input_string


def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def a_link(LinkURL, title, target = '"_self"'):
    return('<a href="' + LinkURL + '" target="' + target + '">' + title + '</a>')


def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>')

def add_space(count):
    return('&nbsp;' * count)

def img_tag(url, title = None, align = None):
    attribute_string = ''
    if(title):
        attribute_string = attribute_string + ' title="' + title + '"'
    else:
        attribute_string = attribute_string + ''

    if(align):
        attribute_string = attribute_string + ' align="' + align + '"'
    else:
        attribute_string = attribute_string + ''

    return '<img src="' + url + '"' + attribute_string + '>'