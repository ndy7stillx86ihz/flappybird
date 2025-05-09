from  commons.abstracts.base_text_renderer import BaseTextRenderer
from  commons.constants import DEFAULT_TITLE_FONT_SIZE, DEFAULT_TITLE_FONT_COLOR, DEFAULT_OPTION_FONT_COLOR, \
    DEFAULT_OPTION_FONT_SIZE, DEFAULT_HOVER_OPTION_FONT_COLOR, DEFAULT_HOVER_OPTION_FONT_SIZE, \
    DEFAULT_OPTIONS_OFFSET, DEFAULT_OUTLINE_WIDTH, DEFAULT_SHADOW_WIDTH, DEFAULT_OUTLINE_COLOR


class MenuRendererMixin(BaseTextRenderer):
    def draw_menu(self, screen, **kwargs):
        screen_width, screen_height = screen.get_size()

        title_params = {
            'font_size': kwargs.get('title_font_size', DEFAULT_TITLE_FONT_SIZE),
            'font_color': kwargs.get('title_font_color', DEFAULT_TITLE_FONT_COLOR),
            'outline_width': kwargs.get('title_outline_width', DEFAULT_OUTLINE_WIDTH),
            'shadow_width': kwargs.get('title_shadow_width', DEFAULT_SHADOW_WIDTH),
            'outline_color': kwargs.get('title_outline_color', DEFAULT_OUTLINE_COLOR)
        }

        caption_params = {
            'font_color': kwargs.get('caption_font_color', DEFAULT_OPTION_FONT_COLOR),
            'font_size': kwargs.get('caption_font_size', DEFAULT_OPTION_FONT_SIZE),
            'options_offset': kwargs.get('caption_options_offset', DEFAULT_OPTIONS_OFFSET),
            'outline_width': kwargs.get('caption_outline_width', DEFAULT_OUTLINE_WIDTH),
            'shadow_width': kwargs.get('caption_shadow_width', DEFAULT_SHADOW_WIDTH - 2),
            'outline_color': kwargs.get('caption_outline_color', DEFAULT_OUTLINE_COLOR),
            'title_margin': kwargs.get('title_margin', screen_height // 10)
        }

        option_params = {
            'font_color': kwargs.get('option_font_color', DEFAULT_OPTION_FONT_COLOR),
            'font_size': kwargs.get('option_font_size', DEFAULT_OPTION_FONT_SIZE),
            'hover_font_color': kwargs.get('option_hover_font_color', DEFAULT_HOVER_OPTION_FONT_COLOR),
            'hover_font_size': kwargs.get('option_hover_font_size', DEFAULT_HOVER_OPTION_FONT_SIZE + 10),
            'options_offset': kwargs.get('options_offset', DEFAULT_OPTIONS_OFFSET),
            'outline_width': kwargs.get('option_outline_width', DEFAULT_OUTLINE_WIDTH),
            'shadow_width': kwargs.get('option_shadow_width', DEFAULT_SHADOW_WIDTH),
            'outline_color': kwargs.get('option_outline_color', DEFAULT_OUTLINE_COLOR),
            'y_forzada': kwargs.get('y_forzada', None)
        }

        self._draw_title(screen, screen_width, screen_height, **title_params)
        self._draw_captions(screen, screen_width, screen_height, **caption_params)
        self._draw_options(screen, screen_width, screen_height, **option_params)

    def _draw_title(self, screen, screen_width, screen_height, font_size, font_color, outline_width, shadow_width,
                    outline_color):
        self.render(screen, (screen_width // 2, screen_height // 5.1), self.menu_title, font_size=font_size,
                    font_color=font_color, outline_width=outline_width, shadow_width=shadow_width,
                    outline_color=outline_color)

    def _draw_captions(self, screen, screen_width, screen_height, font_color, font_size, options_offset, outline_width,
                       shadow_width, outline_color, title_margin):
        title_height = screen_height // 6
        for caption_index, caption in enumerate(self.captions):
            x = screen_width // 2
            y = title_height + title_margin + (caption_index + 1) * options_offset

            self.render(screen, (x, y), caption, font_size=font_size, font_color=font_color,
                        outline_width=outline_width, shadow_width=shadow_width, outline_color=outline_color)

    def _draw_options(self, screen, screen_width, screen_height, font_color, font_size, hover_font_color,
                      hover_font_size, options_offset, outline_width, shadow_width, outline_color, y_forzada=None):
        start_y = screen_height // 5 + len(self.captions) * options_offset + options_offset + screen_height // 20

        for option_index in self.menu_option:
            option_color, option_font_size = (
                hover_font_color, hover_font_size) \
                if option_index == self.selected_option \
                else (font_color, font_size)

            x = screen_width // 2
            y = y_forzada or start_y + option_index.value * options_offset

            self.render(screen, (x, y), option_index.name, font_size=option_font_size, font_color=option_color,
                        outline_width=outline_width, shadow_width=shadow_width, outline_color=outline_color)
