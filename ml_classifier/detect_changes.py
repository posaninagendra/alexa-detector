import pickle
import matplotlib
import sys
import matplotlib.pyplot as plt
import numpy as np

day_start = 1
day_end = 1
results = [dict()] *  (day_end-day_start+1)
for i in range(day_start, day_end+1):
    with open('results' + str(i) + '.pkl') as data_file:
        results[i-day_start] = pickle.load(data_file)
urls = results[0].keys()


def find_var(x):
    return sum((x-np.mean(x))**2)

diff = dict()
var = dict()
var['js'] = []
var['html'] = []
var['dyn'] = []
diff['js'] = []
diff['dyn'] = []
diff['html'] = []

outfile = open('url.txt', 'w')


counter = 0
for url in urls:
    counter += 1
    if counter % 10 == 0:
        print 'url:' + str(counter)
    flag = True
    for i in range(day_start, day_end+1):
        if url not  in results[i-day_start].keys():
            flag = False
    if not flag:
        continue

    for k in var.keys():
        #s = [results[i-day_start][url]['scores'][k] for i in range(day_start, day_end)]

        #var[k].append(find_var(s))
        var[k].append(results[0][url]['scores'][k])
        #if find_var(s) > 0.65333 and k == 'js':
        #    outfile.write(url + ': variance\n')
        for i in range(day_start, day_end):
            diff[k].append(abs(results[i-day_start][url]['scores'][k] - results[i+1-day_start][url]['scores'][k]))
            #if k == 'js' and diff[k][-1] > 0.8:
            #    outfile.write(url + ': diff\n')
    #for i in range(num_of_days - 1):
       # if abs(results[i][url]['scores']['js'] - results[i + 1][url]['scores']['js']) > .3:
            #print url, i

outfile.close()
############## Options to generate nice figures
fig_width_pt = 640.0  # Get this from LaTeX using \showthe\columnwidth
# fig_height_pt = 480.0
inches_per_pt = 1.0 / 72.27  # Convert pt to inch
golden_mean = (np.sqrt(5) - 1.0) / 2.0  # Aesthetic ratio
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width * golden_mean  # height in inches
fig_size = [fig_width, fig_height]

my_yellow = [235. / 255, 164. / 255, 17. / 255]
my_blue = [58. / 255, 93. / 255, 163. / 255]
dark_gray = np.array([68, 84, 106]) / 255.0

my_color = dark_gray  # pick color for theme
params_keynote = {
            'axes.labelsize': 16,
                'font.size': 16,
                    'legend.fontsize': 14,
                        'xtick.labelsize': 14,
                            'ytick.labelsize': 14,
                                'text.usetex': True,
                                    'text.latex.preamble': '\\usepackage{sfmath}',
                                        'font.family': 'sans-serif',
                                            'figure.figsize': fig_size
                                            }
params_ieee = {
            'axes.labelsize': 14,
                'font.size': 14,
                    'legend.fontsize': 12,
                        'xtick.labelsize': 14,
                            'ytick.labelsize': 14,
                                'text.usetex': True,
                                    # 'text.latex.preamble': '\\usepackage{sfmath}',
                                        'font.family': 'serif',
                                            'font.serif': 'ptm',
                                                'figure.figsize': fig_size
                                                }
matplotlib.rcParams.update(params_ieee)

l = {'html':'Html', 'js': 'Static JS', 'dyn': 'Dynamic JS'}

num_of_bins = 25
name = '100 websites'

for k in var.keys():
    y,binEdges=np.histogram(var[k],bins=num_of_bins)
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    plt.plot(bincenters,y,'-', hold = True, label = l[k])
plt.legend()
plt.grid(True, '--')
plt.xlabel('Variance')
plt.title('Histogram of the Scores (' + name +')')
plt.show()

for k in var.keys():
    plt.hist(var[k], bins =num_of_bins )
    plt.grid(True, '--')
    plt.xlabel('Variance')
    plt.title('Histogram of the Score ' + l[k] + ' (' + name +')')
    plt.show()

plt.figure()
for k in var.keys():
    srt = np.sort(var[k])
    print len(var[k])
    print k + " " + str(srt[- 20])
    p = np.arange(0, 1, 1./len(srt))
    plt.plot(srt, p, hold = True, label = l[k])

plt.legend()
plt.grid(True, '--')
plt.xlabel('Variance')
plt.title('CDF of the Scores'+ ' (' + name +')')
plt.show()

# for k in var.keys():
#     y,binEdges=np.histogram(diff[k],bins=num_of_bins)
#     bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
#     plt.plot(bincenters,y,'-', hold = True, label = l[k])
# plt.legend()
# plt.grid(True, '--')
# plt.xlabel('Difference')
# plt.title('Histogram of the Difference of the Scores'+ ' (' + name +')')
# plt.show()
#
# for k in var.keys():
#     plt.hist(diff[k], bins = num_of_bins)
#     plt.grid(True, '--')
#     plt.xlabel('Difference')
#     plt.title('Histogram of the Differences of the Score ' + l[k]+ ' (' + name +')')
#     plt.show()
#
# plt.figure()
# for k in var.keys():
#     srt = np.sort(diff[k])
#     print k + " " + str(srt[-20])
#     p = np.arange(0, 1, 1./len(srt))
#     plt.plot(srt, p, hold = True, label = l[k])
#
# plt.legend()
# plt.grid(True, '--')
# plt.xlabel('Difference')
# plt.title('CDF of the Differences of the Scores'+ ' (' + name +')')
# plt.show()


