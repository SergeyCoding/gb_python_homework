# %% [markdown]
# ## Задача 1.
# Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
#
# По графику определите, при каких значения x значение функции отрицательно.

# %%
import matplotlib.pyplot as plt
import numpy as np


def fun(x):
    return 5*x*x+10*x-30


# %%
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, fun(x))
#plt.plot(x, 0*x)

sp = plt.subplot(111)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x)=5*x^2+10*x-30$')
plt.grid(True)
sp.spines['top'].set_bounds()
sp.spines['right'].set_bounds()
sp.spines['left'].set_position('zero')
sp.spines['bottom'].set_position('zero')

# Подбор значений для определения границ отрицательных значений
specify_bound = (-3.65, 1.65)

plt.bar(specify_bound, height=100, width=0.1, bottom=-50, color='red')

plt.show()

# %%
print(f"Отрицательные значения в диапазоне:{ specify_bound}")
