from app.membership import membership_plans, MembershipType, AdditionalFeature

def calculate_total_cost(base, additional, special=False, premium=False):
    total = base + additional
    if special:
        total -= 20
    if premium:
        total += 50
    return total

def validate_membership(plan, features):
    # Validar que el plan esté en los planes disponibles
    if plan not in membership_plans:
        print(f"Error: El plan '{plan}' no está disponible.")
        return False
    
    # Validar que todas las características seleccionadas estén disponibles en el plan
    available_features = membership_plans[plan]['features']
    for feature in features:
        if feature not in available_features:
            print(f"Error: La característica '{feature}' no está disponible para el plan '{plan}'.")
            return False

    # Si todo es válido, retorna True
    return True