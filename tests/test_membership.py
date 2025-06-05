import pytest
from app.utils import validate_membership
from app.membership import MembershipType, AdditionalFeature

def test_validate_membership_with_valid_plan_and_features():
    assert validate_membership(MembershipType.BASIC, [AdditionalFeature.PERSONAL_TRAINING]) == True
    assert validate_membership(MembershipType.PREMIUM, [AdditionalFeature.PERSONAL_TRAINING, AdditionalFeature.GROUP_CLASSES]) == True

def test_validate_membership_with_invalid_plan():
    assert validate_membership("InvalidPlan", [AdditionalFeature.PERSONAL_TRAINING]) == False

def test_validate_membership_with_invalid_feature():
    assert validate_membership(MembershipType.BASIC, [AdditionalFeature.EXCLUSIVE_ACCESS]) == False
