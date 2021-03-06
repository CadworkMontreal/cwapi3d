from typing import List

from cwapi3d import point_3d


def get_last_error(code: int) -> str: ...
def create_standard_connector(name: str, start: point_3d, end: point_3d) -> int: ...
def get_item_guid_by_name(name: str, number: int) -> str: ...
def get_bolt_length(number: int) -> float: ...
def set_bolt_length(number: int, value: float) -> None: ...
def get_bolt_over_length(number: int) -> float: ...
def set_bolt_over_length(number: int, value: float) -> None: ...
def get_bolt_length_automatic(number: int) -> bool: ...
def set_bolt_length_automatic(number: int, value: bool) -> None: ...
def get_bolt_item_guid(number: int) -> str: ...
def set_bolt_item(number: int, item: str) -> None: ...
def set_diameter(number: int, value: float) -> None: ...
def set_section_diameter(number: int, other_number: int, value: float) -> None: ...
def get_section_diameter(number: int, other_number: int) -> float: ...
def get_axis_items_guids(number: int) -> List[str]: ...
def get_axis_item_name(name: str) -> str: ...
def get_axis_item_material(name: str) -> str: ...
def get_axis_item_norm(name: str) -> str: ...
def get_axis_item_strength_category(name: str) -> str: ...
def get_axis_item_user_field(name: str, number: int) -> str: ...
def get_axis_item_order_number(name: str) -> str: ...
def get_bolt_order_number(number: int) -> str: ...
def check_axis(number: int) -> bool: ...
def clear_errors() -> None: ...
