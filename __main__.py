import voicemeeter

class ManyThings:
    def __init__(self, vmr):
        self.vmr = vmr

    def things(self):
        # Set the mapping of the second input strip
        self.vmr.strip[1].A3 = True
        print(f'Output A4 of Strip {self.vmr.strip[1].label}: {self.vmr.strip[1].A3}')

    def other_things(self):
        # Set the gain slider of the leftmost output bus
        self.vmr.bus[0].gain = -6.0
        print(self.vmr.bus[0].gain)

def main():
    with voicemeeter.remote(kind) as vmr:
        do = ManyThings(vmr)
        do.things()
        do.other_things()

if __name__ == '__main__':
    kind = 'potato'

    # Ensure that Voicemeeter is launched
    voicemeeter.launch(kind)

    main()
