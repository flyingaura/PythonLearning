# -*- coding: utf-8 -*-

def action_test(SubmitValue):
    try:
        if(SubmitValue <= 10):
            Ares = 'GOOD'
        else:
            Ares = 'BAD'
    except ValueError:
        Ares = 'Type Error!'

    return Ares
