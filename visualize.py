import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize(G):

    fig = plt.figure()
    ims = []
    for g in G:
        im = plt.imshow(g, origin='lower')
        ims.append([im])

    im_ani = animation.ArtistAnimation(fig, ims, blit=True)
    plt.show()

    return im_ani
