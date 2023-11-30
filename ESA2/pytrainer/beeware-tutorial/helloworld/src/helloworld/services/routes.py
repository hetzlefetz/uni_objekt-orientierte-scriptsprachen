from enum import StrEnum


class Routes(StrEnum):
    MENU = "menu"
    EXERCISES = "exercises"
    EXERCISES_CREATE = "exercises_create"
    PLANS = "plans"
    PLANS_CREATE = "plans_create"
    PROFILES = "profiles"
    PROFILES_CREATE = "profiles_create"
    WORKOUT = "workout"
    WORKOUT_WHO = "workout_who"
    WORKOUT_WHAT = "workout_what"
    WORKOUT_TRAINING = "workout_training"
    WORKOUT_TRAINING_DETAIL = "workout_training_detail"
