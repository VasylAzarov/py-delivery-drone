class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coord: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coord = coord if coord is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coord[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coord[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coord[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coord[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coord: list[int] = None) -> None:
        if coord is None:
            coord = [0, 0, 0]
        super().__init__(name, weight, coord[:2])
        self.z = coord[2]

    def go_up(self, step: int = 1) -> None:
        self.z += step

    def go_down(self, step: int = 1) -> None:
        self.z -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, coord: list[int] = None,
                 max_load_weight: int = 0, current_load: Cargo = None) -> None:
        super().__init__(name, weight, coord)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
