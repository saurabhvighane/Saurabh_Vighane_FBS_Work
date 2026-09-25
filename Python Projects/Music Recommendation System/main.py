from music_recommendation import MusicRecommendationSystem
from user import User


def choose_option(options, message):
    print(f"\n{message}")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            choice = int(input("Enter choice: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print(
                "Invalid choice. "
                "Please select a valid option."
            )

        except ValueError:
            print("Please enter a number.")


def display_recommendations(recommendations):
    if not recommendations:
        print("\nNo recommendations found.")
        return

    print("\n========== RECOMMENDED SONGS ==========")

    for index, (score, song) in enumerate(
        recommendations,
        start=1
    ):
        print(
            f"\n{index}. "
            f"{song['title']} - {song['artist']}"
        )

        print(f"   Genre: {song['genre']}")
        print(f"   Language: {song['language']}")
        print(f"   Mood: {song['mood']}")


def history_menu(user_system, user_id):
    history = user_system.get_history(user_id)

    if not history:
        print("\nNo recommendation history found.")
        return

    print("\n========== RECOMMENDATION HISTORY ==========")

    for index, record in enumerate(
        history,
        start=1
    ):
        print(
            f"\n{index}. "
            f"Searched: {record['searched_song']}"
        )

        print(
            f"   Recommended: "
            f"{record['recommended_song']} - "
            f"{record['recommended_artist']}"
        )

        print(
            f"   Date: "
            f"{record['recommendation_date']}"
        )


def recommendation_menu(
    system,
    user_system,
    logged_in_user=None
):

    while True:

        song = input(
            "\nEnter a song: "
        ).strip()

        if not song:
            print("Please enter a song name.")
            continue

        results = system.search_song(song)

        if results:

            if len(results) == 1:

                selected_song = results[0]

                print(
                    f"\nSong found: "
                    f"{selected_song['title']} - "
                    f"{selected_song['artist']}"
                )

            else:

                print("\nMultiple songs found:")

                for index, row in enumerate(
                    results,
                    start=1
                ):
                    print(
                        f"{index}. "
                        f"{row['title']} - "
                        f"{row['artist']}"
                    )

                while True:

                    try:
                        choice = int(
                            input("\nSelect a song: ")
                        )

                        if 1 <= choice <= len(results):

                            selected_song = (
                                results[choice - 1]
                            )

                            break

                        print(
                            "Invalid choice. "
                            "Please select a valid "
                            "song number."
                        )

                    except ValueError:
                        print("Please enter a number.")

                print(
                    f"\nSelected song: "
                    f"{selected_song['title']} - "
                    f"{selected_song['artist']}"
                )

            recommendations = (
                system.get_recommendations(
                    selected_song
                )
            )

            display_recommendations(
                recommendations
            )

            if logged_in_user and recommendations:

                user_system.save_history(
                    logged_in_user["user_id"],
                    selected_song["title"],
                    recommendations
                )

        else:

            print("\nSong not found.")

            print(
                "Let's find recommendations "
                "using your preferences."
            )

            genres, languages, moods = (
                system.get_preferences_options()
            )

            genre = choose_option(
                genres,
                "Select Genre:"
            )

            language = choose_option(
                languages,
                "Select Language:"
            )

            mood = choose_option(
                moods,
                "Select Mood:"
            )

            recommendations = (
                system.get_recommendations_by_preferences(
                    genre,
                    language,
                    mood
                )
            )

            display_recommendations(
                recommendations
            )

            if logged_in_user and recommendations:

                user_system.save_history(
                    logged_in_user["user_id"],
                    "Preferences",
                    recommendations
                )

        again = input(
            "\nDo you want to search another song? "
            "(y/n): "
        )

        if again.lower() != "y":
            break


def logged_in_menu(
    system,
    user_system,
    logged_in_user
):

    while True:

        print("\n========================================")
        print(
            f"       WELCOME, "
            f"{logged_in_user['username'].upper()}"
        )
        print("========================================")

        print("1. Get Recommendations")
        print("2. View Recommendation History")
        print("3. Logout")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            recommendation_menu(
                system,
                user_system,
                logged_in_user
            )

        elif choice == "2":

            history_menu(
                user_system,
                logged_in_user["user_id"]
            )

        elif choice == "3":

            print("\nLogged out successfully.")
            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1, 2, or 3."
            )


system = MusicRecommendationSystem()
user_system = User()


while True:

    print("\n========================================")
    print("     MUSIC RECOMMENDATION SYSTEM")
    print("========================================")

    print("1. Register")
    print("2. Login")
    print("3. Continue without Login")
    print("4. Exit")

    choice = input(
        "\nEnter your choice: "
    )

    # REGISTER
    if choice == "1":

        print("\n========== REGISTER ==========")

        username = input(
            "Enter username: "
        ).strip()

        password = input(
            "Enter password: "
        )

        confirm_password = input(
            "Confirm password: "
        )

        if not username or not password:

            print(
                "\nUsername and password "
                "cannot be empty."
            )

        elif password != confirm_password:

            print("\nPasswords do not match.")

        elif user_system.register(
            username,
            password
        ):

            print("\nRegistration successful!")

        else:

            print(
                "\nUsername already exists."
            )

    # LOGIN
    elif choice == "2":

        print("\n============ LOGIN ============")

        username = input(
            "Enter username: "
        ).strip()

        password = input(
            "Enter password: "
        )

        logged_in_user = user_system.login(
            username,
            password
        )

        if logged_in_user:

            print(
                f"\nLogin successful! "
                f"Welcome, "
                f"{logged_in_user['username']}!"
            )

            logged_in_menu(
                system,
                user_system,
                logged_in_user
            )

        else:

            print(
                "\nInvalid username or password."
            )

    # CONTINUE WITHOUT LOGIN
    elif choice == "3":

        print(
            "\nContinuing without login..."
        )

        recommendation_menu(
            system,
            user_system
        )

    # EXIT
    elif choice == "4":

        print(
            "\nThank you for using "
            "Music Recommendation System!"
        )

        break

    else:

        print(
            "\nInvalid choice. "
            "Please select 1, 2, 3, or 4."
        )


system.close_connection()
user_system.close_connection()