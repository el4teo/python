import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox

INTIAL_WINDOW_ZOOMED = False
HIDE_TOOL_BAR = True
LOG_SCALE = False

def main():
    # Configure fig
    fig = plt.figure(figsize=(8,4.5),num='TITLE HERE')
    mng = plt.get_current_fig_manager()

    if INTIAL_WINDOW_ZOOMED:
        mng.window.state('zoomed')
    if HIDE_TOOL_BAR:
        fig.canvas.toolbar.pack_forget()

    # Create an ax
    base_offset_x = 0.125
    base_offset_y = 0.15
    ax_wdith = 0.775
    ax_high = 0.75
    ax = fig.add_axes([base_offset_x, base_offset_y, ax_wdith, ax_high])
    ax.set_title('AXES  TITLE')
    ax.set_xlabel('X LABEL')
    ax.set_ylabel('Y LABEL')
    ax.set_facecolor('lightgoldenrodyellow')
    ax.set_xlim(0, 360)
    ax.set_xticks([0, 90, 180, 270, 360])
    ax.set_ylim(-1, 1)
    if LOG_SCALE:
        ax.set_yscale('log')
    ax.tick_params(axis='both',labelsize=10)
    ax.grid(visible=True, which='both', axis='both', linestyle='--')

    # Basic plot in the ax
    x = [0, 90, 180, 270, 360]
    y = [0, 1, 0, -1, 0]
    h_plot = ax.plot(x, y, color='#9A0000')
    h_scatter = ax.scatter(x, y, color='#001E9A', marker='o', s=40)

    # Run plt.draw() in case you want to instantaneously update the plot
    plt.draw()
        
    # Run plt.show() at the end . It interrupts the program flow
    plt.show()

if __name__ == "__main__":
    main()