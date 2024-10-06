import matplotlib.pyplot as plt

def genDates(num : int, startYear : int) -> list[str]:

    '''generates x ticks in form of list ['year month', 'year month', 'year month', ...] and returns the list'''

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    dates = []
    year = startYear -1
    for i in range(num):
        if i % 12 == 0:
            year += 1
        dates.append(f'{year} {months[i % 12]}')
    return dates


def drawGraph(title : str, x : list, y : list):
    
    '''displays matplotlib graph'''

    plt.plot(x, y)
    plt.title(title)
    plt.show()