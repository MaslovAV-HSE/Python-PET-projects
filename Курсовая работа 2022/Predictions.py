variants = ["Результаты при отказе от курения", "Резулльтате если начать курить",
            "и при отказе от спорта: ", "и при занятиях спортом: " ]

def MakePredictions(results:list):
    text = []
    results[0] = str(int(results[0]) + 10)

    if results[19] == 0:
        results[19] = 1
        text.append(variants[1])
    else:
        text.append(variants[0])
        results[19] = 0

    if results[20] == 1:
        results[20] = 0
        text.append(variants[2])
    else:
        results[20] = 1
        text.append(variants[3])
    txt = " ".join(text)
    return results, txt







