import datetime
import json

class TravelPlanner:
    """Simple travel itinerary generator for demo & testing.

    NOTE: Uses placeholder data. Real-world apps should call APIs or databases.
    """

    def __init__(self):
        # Placeholder data - In a real app, this would come from databases/APIs
        self.destinations_around_india = {
            "Nepal": {
                "low": {"cost_per_day": 30, "pois": ["Pashupatinath Temple", "Boudhanath Stupa", "Kathmandu Durbar Square"]},
                "medium": {"cost_per_day": 70, "pois": ["Everest Base Camp Trek", "Pokhara Lakeside", "Chitwan National Park"]},
                "high": {"cost_per_day": 150, "pois": ["Luxury Everest Heli Tour", "Boutique stays in Kathmandu"]}
            },
            "Sri Lanka": {
                "low": {"cost_per_day": 40, "pois": ["Galle Fort", "Unawatuna Beach", "Sigiriya"]},
                "medium": {"cost_per_day": 80, "pois": ["Kandy Temple of Tooth", "Ella scenic trains", "Yala National Park Safari"]},
                "high": {"cost_per_day": 180, "pois": ["Luxury resorts in Bentota", "Hot air ballooning in Dambulla"]}
            },
            # ... more destinations
        }
        self.poi_details = { # Simple details for demonstration
            "Pashupatinath Temple": {"interest": "Monuments", "duration": 2, "cost": 5, "type": "cultural"},
            "Boudhanath Stupa": {"interest": "Monuments", "duration": 1.5, "cost": 3, "type": "cultural"},
            "Kathmandu Durbar Square": {"interest": "Monuments", "duration": 2.5, "cost": 8, "type": "cultural"},
            "Everest Base Camp Trek": {"interest": "Adventure", "duration": 10, "cost": 500, "type": "trekking"},
            "Pokhara Lakeside": {"interest": "Nature", "duration": 3, "cost": 10, "type": "leisure"},
            "Galle Fort": {"interest": "Monuments", "duration": 3, "cost": 5, "type": "historic"},
            "Unawatuna Beach": {"interest": "Nature", "duration": 4, "cost": 10, "type": "leisure"},
            "Sigiriya": {"interest": "Monuments", "duration": 3, "cost": 20, "type": "historic"},
            "Kandy Temple of Tooth": {"interest": "Monuments", "duration": 2, "cost": 10, "type": "cultural"},
            "Ella scenic trains": {"interest": "Travel", "duration": 3, "cost": 5, "type": "scenic"},
            "Yala National Park Safari": {"interest": "Nature", "duration": 4, "cost": 40, "type": "wildlife"},
            # ... more POIs
        }
        self.transport_costs = { # Per day estimate
            "Bus": {"low": 10, "medium": 15, "high": 20},
            "Train": {"low": 15, "medium": 25, "high": 40},
            "Flight": {"low": 50, "medium": 100, "high": 200}, # This would be per leg, not per day
            "Car": {"low": 30, "medium": 60, "high": 100},
        }
        self.stay_costs = { # Per night estimate
            "Lodge": {"low": 20, "medium": 40, "high": 70},
            "House": {"low": 30, "medium": 60, "high": 100},
            "Hotel": {"low": 40, "medium": 80, "high": 150},
        }

    def generate_itinerary(self, destination_topic, duration, budget_level,
                          preferred_transport=None, preferred_stay=None, interests=None, start_date=None):

        # Contract:
        # - Inputs: destination_topic (str), duration (int days), budget_level ('low'|'medium'|'high'),
        #   preferred_transport (list of str), preferred_stay (list of str), interests (list of str), start_date (str dd-MMM-YYYY)
        # - Output: dict with 'summary' and 'itinerary_details' or {'error': msg}

        # 1. Input Validation (basic)
        if destination_topic not in self.destinations_around_india:
            return {"error": "Destination not supported yet."}
        if not isinstance(duration, int) or duration <= 0:
            return {"error": "Duration must be at least 1 day."}
        if budget_level not in ["low", "medium", "high"]:
            return {"error": "Invalid budget level."}

        preferred_transport = preferred_transport or []
        preferred_stay = preferred_stay or []
        interests = interests or []

        # 2. Budget Allocation (simplified)
        daily_budget = self.destinations_around_india[destination_topic][budget_level]["cost_per_day"]
        total_budget = daily_budget * duration

        # Estimate accommodation cost (simplistic: average of preferred types)
        avg_stay_cost_per_night = 0
        if preferred_stay:
            count = 0
            for stay_type in preferred_stay:
                if stay_type in self.stay_costs:
                    avg_stay_cost_per_night += self.stay_costs[stay_type][budget_level]
                    count += 1
            avg_stay_cost_per_night = (avg_stay_cost_per_night / count) if count else 0
import datetime
import json


class TravelPlanner:
    """Simple travel itinerary generator for demo & testing.

    NOTE: Uses placeholder data. Real-world apps should call APIs or databases.
    """

    def __init__(self):
        # Placeholder data - In a real app, this would come from databases/APIs
        self.destinations_around_india = {
            "Nepal": {
                "low": {"cost_per_day": 30, "pois": ["Pashupatinath Temple", "Boudhanath Stupa", "Kathmandu Durbar Square"]},
                "medium": {"cost_per_day": 70, "pois": ["Everest Base Camp Trek", "Pokhara Lakeside", "Chitwan National Park"]},
                "high": {"cost_per_day": 150, "pois": ["Luxury Everest Heli Tour", "Boutique stays in Kathmandu"]}
            },
            "Sri Lanka": {
                "low": {"cost_per_day": 40, "pois": ["Galle Fort", "Unawatuna Beach", "Sigiriya"]},
                "medium": {"cost_per_day": 80, "pois": ["Kandy Temple of Tooth", "Ella scenic trains", "Yala National Park Safari"]},
                "high": {"cost_per_day": 180, "pois": ["Luxury resorts in Bentota", "Hot air ballooning in Dambulla"]}
            },
        }
        self.poi_details = {  # Simple details for demonstration
            "Pashupatinath Temple": {"interest": "Monuments", "duration": 2, "cost": 5, "type": "cultural"},
            "Boudhanath Stupa": {"interest": "Monuments", "duration": 1.5, "cost": 3, "type": "cultural"},
            "Kathmandu Durbar Square": {"interest": "Monuments", "duration": 2.5, "cost": 8, "type": "cultural"},
            "Everest Base Camp Trek": {"interest": "Adventure", "duration": 10, "cost": 500, "type": "trekking"},
            "Pokhara Lakeside": {"interest": "Nature", "duration": 3, "cost": 10, "type": "leisure"},
            "Galle Fort": {"interest": "Monuments", "duration": 3, "cost": 5, "type": "historic"},
            "Unawatuna Beach": {"interest": "Nature", "duration": 4, "cost": 10, "type": "leisure"},
            "Sigiriya": {"interest": "Monuments", "duration": 3, "cost": 20, "type": "historic"},
            "Kandy Temple of Tooth": {"interest": "Monuments", "duration": 2, "cost": 10, "type": "cultural"},
            "Ella scenic trains": {"interest": "Travel", "duration": 3, "cost": 5, "type": "scenic"},
            "Yala National Park Safari": {"interest": "Nature", "duration": 4, "cost": 40, "type": "wildlife"},
        }
        self.transport_costs = {  # Per day estimate
            "Bus": {"low": 10, "medium": 15, "high": 20},
            "Train": {"low": 15, "medium": 25, "high": 40},
            "Flight": {"low": 50, "medium": 100, "high": 200},
            "Car": {"low": 30, "medium": 60, "high": 100},
        }
        self.stay_costs = {  # Per night estimate
            "Lodge": {"low": 20, "medium": 40, "high": 70},
            "House": {"low": 30, "medium": 60, "high": 100},
            "Hotel": {"low": 40, "medium": 80, "high": 150},
        }

    def generate_itinerary(self, destination_topic, duration, budget_level,
                           preferred_transport=None, preferred_stay=None, interests=None, start_date=None):

        # Contract:
        # - Inputs: destination_topic (str), duration (int days), budget_level ('low'|'medium'|'high'),
        #   preferred_transport (list of str), preferred_stay (list of str), interests (list of str), start_date (str dd-MMM-YYYY)
        # - Output: dict with 'summary' and 'itinerary_details' or {'error': msg}

        # 1. Input Validation (basic)
        if destination_topic not in self.destinations_around_india:
            return {"error": "Destination not supported yet."}
        if not isinstance(duration, int) or duration <= 0:
            return {"error": "Duration must be at least 1 day."}
        if budget_level not in ["low", "medium", "high"]:
            return {"error": "Invalid budget level."}

        preferred_transport = preferred_transport or []
        preferred_stay = preferred_stay or []
        interests = interests or []

        # 2. Budget Allocation (simplified)
        daily_budget = self.destinations_around_india[destination_topic][budget_level]["cost_per_day"]
        total_budget = daily_budget * duration

        # Estimate accommodation cost (simplistic: average of preferred types)
        avg_stay_cost_per_night = 0
        if preferred_stay:
            count = 0
            for stay_type in preferred_stay:
                if stay_type in self.stay_costs:
                    avg_stay_cost_per_night += self.stay_costs[stay_type][budget_level]
                    count += 1
            avg_stay_cost_per_night = (avg_stay_cost_per_night / count) if count else 0

        accommodation_budget = avg_stay_cost_per_night * duration

        # Estimate transport cost (simplistic: average of preferred types per day)
        avg_transport_cost_per_day = 0
        if preferred_transport:
            count = 0
            for transport_type in preferred_transport:
                if transport_type in self.transport_costs:
                    avg_transport_cost_per_day += self.transport_costs[transport_type][budget_level]
                    count += 1
            avg_transport_cost_per_day = (avg_transport_cost_per_day / count) if count else 0

        transport_budget = avg_transport_cost_per_day * duration

        remaining_budget_for_activities_food = total_budget - accommodation_budget - transport_budget
        daily_activity_food_budget = remaining_budget_for_activities_food / duration if duration else 0

        # 3. POI Selection & Daily Itinerary Construction (highly simplified)
        itinerary = []
        # If no interests provided, fall back to all POIs for that budget
        candidates = self.destinations_around_india[destination_topic][budget_level]["pois"]
        if interests:
            available_pois = [
                poi for poi in candidates
                if any(interest == self.poi_details.get(poi, {}).get("interest") for interest in interests)
            ]
        else:
            available_pois = list(candidates)

        if not available_pois:
            return {"error": "No POIs found matching your interests and destination for this budget."}

        try:
            current_date = datetime.datetime.strptime(start_date, "%d-%b-%Y").date() if start_date else datetime.date.today()
        except Exception:
            return {"error": "start_date must be in format DD-MMM-YYYY (e.g. 01-Sep-2024)."}

        # Rotate POIs if trip is longer than POIs list
        poi_pool = list(available_pois)

        for day in range(1, duration + 1):
            day_activities = []
            day_budget_spent = 0

            # Select up to 2 POIs per day
            for _ in range(2):
                if not poi_pool:
                    poi_pool = list(available_pois)
                if poi_pool:
                    poi_name = poi_pool.pop(0)
                    poi_info = self.poi_details.get(poi_name, {})

                    if day_budget_spent + poi_info.get("cost", 0) <= daily_activity_food_budget * 1.5:
                        day_activities.append({
                            "name": poi_name,
                            "interest": poi_info.get("interest"),
                            "duration_hours": poi_info.get("duration"),
                            "estimated_cost": poi_info.get("cost")
                        })
                        day_budget_spent += poi_info.get("cost", 0)

            itinerary.append({
                "day": day,
                "date": current_date.strftime("%d %b, %Y"),
                "location": destination_topic,
                "activities": day_activities,
                "food_suggestions": f"Explore local eateries for around {max(0, daily_activity_food_budget - day_budget_spent):.2f} {destination_topic} Currency",
                "accommodation": f"{preferred_stay[0] if preferred_stay else 'Lodge'} in {destination_topic} area (est. {avg_stay_cost_per_night:.2f} {destination_topic} Currency)",
                "daily_transport_mode": preferred_transport[0] if preferred_transport else "Local Bus",
                "estimated_daily_cost": (daily_activity_food_budget + avg_stay_cost_per_night + avg_transport_cost_per_day)
            })

            current_date += datetime.timedelta(days=1)

        final_itinerary = {
            "summary": {
                "destination": destination_topic,
                "duration": f"{duration} days",
                "start_date": start_date if start_date else "Today",
                "budget_level": budget_level,
                "total_estimated_cost": total_budget,
                "preferred_transport": ", ".join(preferred_transport) if preferred_transport else "N/A",
                "preferred_stay": ", ".join(preferred_stay) if preferred_stay else "N/A",
                "interests": ", ".join(interests) if interests else "N/A"
            },
            "itinerary_details": itinerary
        }

        return final_itinerary


if __name__ == "__main__":
    planner = TravelPlanner()

    # User inputs
    destination = "Sri Lanka"
    start = "01-Sep-2024"
    days = 7
    budget = "medium"
    transport = ["Bus", "Train"]
    stay = ["Lodge"]
    user_interests = ["Monuments", "Nature", "Travel"]

    generated_trip = planner.generate_itinerary(
        destination_topic=destination,
        duration=days,
        budget_level=budget,
        preferred_transport=transport,
        preferred_stay=stay,
        interests=user_interests,
        start_date=start
    )

    if "error" in generated_trip:
        print(f"Error: {generated_trip['error']}")
    else:
        print(json.dumps(generated_trip, indent=4))
