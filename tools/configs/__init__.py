from pixel_font_knife import glyph_mapping_util
from pixel_font_knife.kerning_util import KerningConfig

from tools.configs import options, path_define
from tools.configs.dump import DumpConfig
from tools.configs.fallback import FallbackConfig
from tools.configs.font import FontConfig

version = '2026.01.01'

dump_configs = DumpConfig.load()

fallback_configs = FallbackConfig.load()

font_configs = {font_size: FontConfig.load(font_size) for font_size in options.font_sizes}

mappings = [
    glyph_mapping_util.load_mapping(path_define.mappings_dir.joinpath('2E80-2EFF CJK Radicals Supplement.yaml')),
    glyph_mapping_util.load_mapping(path_define.mappings_dir.joinpath('2F00-2FDF Kangxi Radicals.yaml')),
]

kerning_config = KerningConfig.load(path_define.kernings_dir.joinpath('default.yaml'))

locale_to_language_flavor = {
    'en': 'latin',
    'zh-hans': 'zh_hans',
    'zh-hant': 'zh_hant',
    'ja': 'ja',
    'ko': 'ko',
}
