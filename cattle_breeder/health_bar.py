
import pygame

class Health_Bar():
	"""A class to represent the health bar of a cow"""
	
	def __init__(self, cb_settings, cow, screen):
		"""initializes the health bar"""
		self.cow = cow
		self.cb_settings = cb_settings
		self.screen_rect = screen.get_rect()
		# Set dimensions of health bar and its color
		self.width, self.height = self.cow.rect.width, 5
		self.health_bar_color = (0, 0, 0)
		# Build the rect and position it above cow
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = self.cow.rect.centerx
		self.rect.bottom = self.cow.rect.top
		
	def draw_button(self):
		# Draw a full health bar
		self.screen.fill(self.button_color, self.rect)
		
		
