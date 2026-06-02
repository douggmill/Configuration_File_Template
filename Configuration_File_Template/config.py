# config_reader.py

from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class InitializationConfig:
    ramp_up_current_Max: float
    positive_5V_max: float
    positive_5V_min: float
    negative_5V_max: float
    negative_5V_min: float
    CLKIN_HIGH_CURRENT_MAX: float
    CLKIN_LOW_VOLTAGE_MAX: float
    positive_5V_CLKIN_max: float
    positive_5V_CLKIN_min: float
    positive_5V_DATAOUT_max: float
    positive_5V_DATAOUT_min: float
    DATAIN_HIGH_CURRENT_MAX: float
    DATAIN_HIGH_VOLTAGE_MAX: float
    positive_5V_DATAIN_max: float
    positive_5V_DATAIN_min: float
    AUXIN_max: float
    AUXIN_min: float
    save_path: str


def read_initialization_file(file_path: str) -> InitializationConfig:
    parser = ConfigParser()

    # ConfigParser requires a section header
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = "[DEFAULT]\n" + f.read()

    parser.read_string(file_content)

    cfg = parser["DEFAULT"]

    return InitializationConfig(
        ramp_up_current_Max=cfg.getfloat("ramp_up_current_Max"),
        positive_5V_max=cfg.getfloat("positive_5V_max"),
        positive_5V_min=cfg.getfloat("positive_5V_min"),
        negative_5V_max=cfg.getfloat("negative_5V_max"),
        negative_5V_min=cfg.getfloat("negative_5V_min"),
        CLKIN_HIGH_CURRENT_MAX=cfg.getfloat("CLKIN_HIGH_CURRENT_MAX"),
        CLKIN_LOW_VOLTAGE_MAX=cfg.getfloat("CLKIN_LOW_VOLTAGE_MAX"),
        positive_5V_CLKIN_max=cfg.getfloat("positive_5V_CLKIN_max"),
        positive_5V_CLKIN_min=cfg.getfloat("positive_5V_CLKIN_min"),
        positive_5V_DATAOUT_max=cfg.getfloat("positive_5V_DATAOUT_max"),
        positive_5V_DATAOUT_min=cfg.getfloat("positive_5V_DATAOUT_min"),
        DATAIN_HIGH_CURRENT_MAX=cfg.getfloat("DATAIN_HIGH_CURRENT_MAX"),
        DATAIN_HIGH_VOLTAGE_MAX=cfg.getfloat("DATAIN_HIGH_VOLTAGE_MAX"),
        positive_5V_DATAIN_max=cfg.getfloat("positive_5V_DATAIN_max"),
        positive_5V_DATAIN_min=cfg.getfloat("positive_5V_DATAIN_min"),
        AUXIN_max=cfg.getfloat("AUXIN_max"),
        AUXIN_min=cfg.getfloat("AUXIN_min"),
        save_path=cfg.get("save_path").strip('"')
    )


if __name__ == "__main__":
    config = read_initialization_file("initialization.txt")

    print(config)

    print("AUXIN MAX:", config.AUXIN_max)
    print("Save Path:", config.save_path)