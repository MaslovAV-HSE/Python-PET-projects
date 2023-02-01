
import matplotlib.pyplot as plt

x = ['Инфаркт\nмиокардо', 'Стенокардия\nстабильная', 'Стенокардия\nнестабильная', 'Ишемическая\nболезнь\nсердца',
     'Гипертоническая\nболезнь\nсердца', 'Аритмии\nи\nблокады\nсердца', "Хроническая\nсердечная\nнедостаточность", 'Ишемическа\nсердечная\nнедостаточность', '']

res = [13.11, 6.01, 4.39, 10.2, 3.32, 0.98, 6.45]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def make_pic(res):
     list(res)
     res.insert(3, max(res[0], res[1], res[2]))
     res.append(100)
     fig, ax = plt.subplots()
     ax.bar(x, res, color=['red', 'green', 'blue', 'purple', 'yellow', 'gray', 'orange', 'lightgreen', 'white'])
     fig.set_figwidth(20)  # ширина и
     fig.set_figheight(10)  # высота "Figure"
     fig.set_facecolor('floralwhite')
     ax.set_facecolor('white')
     name = str('result.png')
     plt.savefig(name, bbox_inches='tight')
     return  name


"""
plt.bar(x, res, x=y)

"""