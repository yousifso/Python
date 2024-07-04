import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# Fetch Rottweiler tail length data and calculate mean and standard deviation
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
rottweiler_tl_mean = np.mean(rottweiler_tl)
rottweiler_tl_std = np.std(rottweiler_tl)

# Fetch Whippet rescue data and perform a binomial test
whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
print(binom_test(num_whippet_rescues, num_whippets, .08))

# Fetch weights for Whippets, Terriers, and Pitbulls and perform ANOVA and Tukey's range test
w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")
print(f_oneway(w, t, p).pvalue)

values = np.concatenate([w, t, p])
labels = ["whippet"] * len(w) + ["terrier"] * len(t) + ["pitbull"] * len(p)
print(pairwise_tukeyhsd(values, labels, .05))

# Fetch color data for Poodles and Shih Tzus and perform Chi-square test
poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")
color_table = [
  [np.count_nonzero(poodle_colors == "Black"), np.count_nonzero(shihtzu_colors == "Black")],
  [np.count_nonzero(poodle_colors == "Brown"), np.count_nonzero(shihtzu_colors == "Brown")],
  [np.count_nonzero(poodle_colors == "Gold"), np.count_nonzero(shihtzu_colors == "Gold")],
  [np.count_nonzero(poodle_colors == "Grey"), np.count_nonzero(shihtzu_colors == "Grey")],
  [np.count_nonzero(poodle_colors == "White"), np.count_nonzero(shihtzu_colors == "White")]
]
print(chi2_contingency(color_table))
