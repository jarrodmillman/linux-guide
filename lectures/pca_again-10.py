# Show first vector as sum of x and y axis vectors
x, y = v1
# Make subplots for vectors and text
fig, (vec_ax, txt_ax) = plt.subplots(1, 2, figsize=(14, 4))
# Plot 0, 0
vec_ax.plot(0, 0, 'ro')
# Show vectors as arrows
vec_ax.arrow(0, 0, x, 0, color='r', length_includes_head=True, width=0.01)
vec_ax.arrow(0, 0, x, y, color='k', length_includes_head=True, width=0.01)
vec_ax.arrow(x, 0, 0, y, color='b', length_includes_head=True, width=0.01)
# Label origin
vec_ax.annotate('$(0, 0)$', (-0.3, -0.3), fontsize=16)
# Label vectors
vec_ax.annotate(r'$\vec{{v_1}} = ({x:.2f}, {y:.2f})$'.format(x=x, y=y),
                (x / 2 - 2.2, y / 2), fontsize=16)
vec_ax.annotate(r'$\vec{{x}} = ({x:.2f}, 0)$'.format(x=x),
                (x / 2 - 0.5, -0.3), fontsize=16)
vec_ax.annotate(r'$\vec{{y}} = (0, {y:.2f})$'.format(y=y),
                (x + 0.1, y / 2 - 0.1), fontsize=16)
# Make sure axes are correct lengths
vec_ax.axis((-1, 5.5, -1, 3))
vec_ax.set_aspect('equal', adjustable='box')
vec_ax.set_title(r'x- and y- axis components of $\vec{v_1}$')
# Text about lengths
txt_ax.axis('off')
txt_ax.annotate(r'$\|\vec{v_1}\|^2 = \|\vec{x}\|^2 + \|\vec{y}\|^2$ =' +
                '${x:.2f}^2 + {y:.2f}^2$'.format(x=x, y=y),
                (0, 0.5), fontsize=16)
# ...
