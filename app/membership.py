from enum import Enum

class MembershipType(Enum):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
    FAMILY = 'Family'

class AdditionalFeature(Enum):
    PERSONAL_TRAINING = 'Personal Training Sessions'
    GROUP_CLASSES = 'Group Classes'
    EXCLUSIVE_ACCESS = 'Exclusive Gym Facilities'
    SPECIAL_TRAINING = 'Specialized Training Programs'

membership_plans = {
    MembershipType.BASIC: {
        'base_cost': 50,
        'features': {
            AdditionalFeature.PERSONAL_TRAINING: 20,
            AdditionalFeature.GROUP_CLASSES: 15
        }
    },
    MembershipType.PREMIUM: {
        'base_cost': 100,
        'features': {
            AdditionalFeature.PERSONAL_TRAINING: 30,
            AdditionalFeature.GROUP_CLASSES: 25,
            AdditionalFeature.EXCLUSIVE_ACCESS: 40,
            AdditionalFeature.SPECIAL_TRAINING: 35
        }
    },
    MembershipType.FAMILY: {
        'base_cost': 150,
        'features': {
            AdditionalFeature.GROUP_CLASSES: 20
        }
    }
}

class Membership:
    def __init__(self):
        self.selected_plan = None

    def get_available_plans(self):
        # Retorna los valores de MembershipType
        return [plan for plan in MembershipType]

    def select_plan(self, plan_name):
        try:
            self.selected_plan = MembershipType(plan_name)
        except ValueError:
            raise ValueError(f"Plan de membresía '{plan_name}' no disponible.")
        return self  # Devuelve el objeto actual
