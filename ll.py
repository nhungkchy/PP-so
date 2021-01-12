from sklearn.linear_model import LinearRegression

excel_file = 'vdd.xlsx' # truyền file excel với bảng dữ liệu x,y
data = pd.read_excel(excel_file, index = False).values
data = np.array(data)
data_sort_x_y = data_sort.transpose()
x = data[0]
y = data[1]
lm = LinearRegression()
lm.fit(x, y)


plt.scatter(x, y)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.savefig('đ.png')
plt.show()