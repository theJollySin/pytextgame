'''Minimal sketch of pytextgame apps'''


class Game(object):

    def __init__(self):
        self._situations = {}
        self._situation = None
        self._text_entry = False
        self._redraw = True
        self._new_ui = False
        self._events  = []

    def text_entry(self):
        '''getter: Are we in a text entry game state?'''
        return self._text_entry

    def set_set_entry(self, boolean):
        '''setter: Are we in a text entry game state?'''
        self._text_entry = boolean

    def new_ui(self):
        '''returns False or a string keyword for the new UI'''
        return self._new_ui

    def set_new_ui(self, ui_str):
        '''Setter for new UI representative string'''
        self._new_ui = ui_str

    def set_redraw(self, needs_redraw):
        '''This sets the hook attribute: if the game state changes in a
        way that is visible on the screen, you will want to redraw the screen.
        '''
        self._redraw = needs_redraw

    def redraw(self):
        '''getter for the redraw attribute"'''
        return self._redraw

    def start(self):
        '''Start the game'''
        self._new_ui = False
        self.do_start()

    def stop(self):
        '''Stop the game'''
        self.do_stop()
        self._new_ui = False

    def do_turn(self, time_passed=0):
        '''The meat of the game logic will go here'''
        raise Exception("Not Implemented")

    def do_start(self):
        '''Perform initial setup of the Game and state'''
        pass

    def do_stop(self):
        '''A convience method, perhaps you always want to save
        when the game is stopped, or you need to clean up your
        cache/database. Do so here.
        '''
        pass

    def add_events(self, events):
        '''Add events to the queue'''
        self._events += events

    def new_events(self):
        '''Pull all possible events and clear out the queue'''
        events = self._events
        self._events = []

        return events

    def situation(self):
        '''get the current Situation of the game'''
        return self._situation

    def set_situation(self, situation_str):
        '''set the current Situation of the game'''
        self.situation = self._situations[situation_str](self)

    def resolve_situation(self, situation):
        '''Allow the situation to modify the game state'''
        raise Exception("Not Implemented")

    def available_actions(self):
        '''Return a list of actions that are currently valid'''
        raise Exception("Not Implemented")

    def text_entry_action(self, key):
        '''Text Entry requires a different kind of Action than a
        normal game interaction.
        '''
        raise Exception('Not Implemented')
