from pathlib import Path
import time

from playsound import playsound


CLEAR = "\033[2J\033[H"


def alarm(seconds: int) -> None:
	time_elapsed = 0
	print(CLEAR, end="")

	while time_elapsed < seconds:
		time.sleep(1)
		time_elapsed += 1
		time_left = seconds - time_elapsed
		minutes_left = time_left // 60
		seconds_left = time_left % 60
		print(
			f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}",
			end="",
			flush=True,
		)

	print("\nTime is up!")
	sound_file = Path(__file__).with_name("alarm.mp3")
	playsound(str(sound_file))


def main() -> None:
	minutes = int(input("How many minutes to wait: "))
	seconds = int(input("How many seconds to wait: "))
	total_seconds = minutes * 60 + seconds
	alarm(total_seconds)


if __name__ == "__main__":
	main()