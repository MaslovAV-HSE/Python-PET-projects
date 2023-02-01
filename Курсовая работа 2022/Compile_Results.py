import Person, NS_Connection,Diagrams

def Results(result: list ):
    message = 'Наличие сердечно-сосудистого заболевания маловероятно.'
    img_name = Diagrams.make_pic(result.copy())
    if max(result)> 40:
        message = 'Возможно наличие заболевания!\nРекомендуется консультация кардиолога.'
    if sum(result) > 70*8:
        message = 'Ситуация критическая!\nРекомендуется немедленная консультация кардиолога.'

    return message, img_name