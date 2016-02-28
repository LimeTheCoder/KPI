from controller import Controller, Model

model = Model('data.txt')
controller = Controller(model)
controller.run()