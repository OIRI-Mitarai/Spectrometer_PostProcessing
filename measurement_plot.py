import os
import pandas as pd
import matplotlib.pyplot as plt


# csv data directory
data_folder = 'data'

# get csv file name in direvtory
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.txt')]

# prepare plot
plt.figure(figsize=(8, 6))

# load all csv file and plot them
for file in csv_files:
    file_path = os.path.join(data_folder, file)

    # load csv data
    df = pd.read_csv(file_path, encoding='cp932', skiprows=1)

    # for debug
    '''
    print('--------------')
    print(file, df.shape)
    print(df.head())
    print('--------------')
    '''

    # legend label from file name(except '.csv')
    label = file.replace('.txt', '')

    # plot
    '''
    df.iloc[:, 0] -> 1st row "波長[nm]"
    df.iloc[:, 1] -> 2nd row "透過率[%]"
    標記が人により異なるため列番号で指定
    '''
    plt.plot(df.iloc[:, 0], df.iloc[:, 1], label=label)

# axis label
# plt.xlabel('波長[nm]', fontsize=12, fontname='MS Gothic')
# plt.ylabel('透過率[%]', fontsize=12, fontname='MS Gothic')

# Y-axis range
plt.ylim(0, 100)

# legend label
# plt.legend(prop={'family':'MS Gothic'})


from matplotlib import font_manager, rcParams
font_path = "./YuGothL.ttc"
font_prop = font_manager.FontProperties(fname=font_path)
rcParams['font.family'] = font_prop.get_name()
plt.xlabel('波長[nm]', fontsize=12, fontproperties=font_prop)
plt.ylabel('透過率[%]', fontsize=12, fontproperties=font_prop)
plt.legend(prop=font_prop)


# display grid
plt.grid(True)

# save plot
plt.savefig('Graph_plot.png')

# show plot
plt.show()

plt.close('all')
