import argparse
import parser
import sys

from client import DiscogsClient


def parse_args():
    """
    Parses command line arguments using argparse.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog="diggerpy",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-t",
        "--token",
        help="Discogs API token (required)",
        required=True,
    )

    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument(
        "query",
        help="The search query",
    )

    artist_parser = subparsers.add_parser("artist")
    artist_parser.add_argument(
        "id",
        type=int,
        help="The artist ID",
    )

    label_parser = subparsers.add_parser("label")
    label_parser.add_argument(
        "id",
        type=int,
        help="The label ID",
    )

    release_parser = subparsers.add_parser("release")
    release_parser.add_argument(
        "id",
        type=int,
        help="The release ID",
    )

    return parser.parse_args()


def main():
    """
    The main entry point of the `diggerpy` command line tool.

    Parses command line arguments, creates a DiscogsClient instance using the provided API token,
    and dispatches the appropriate subcommand.
    """
    args = parse_args()
    client = DiscogsClient(token=args.token)

    if args.command == "search":
        results = client.search(args.query)
        for result in results.results:
            print(f"{result.type.capitalize()}: {result.title} ({result.year})")
            if hasattr(result, "main_release"):
                print(f"Main Release ID: {result.main_release.id}")
            print()

    elif args.command == "artist":
        artist = client.get_artist(args.id)
        print(f"Name: {artist.name}")
        print(f"Profile: {artist.profile}")

    elif args.command == "label":
        label = client.get_label(args.id)
        print(f"Name: {label.name}")
        print(f"Profile: {label.profile}")

    elif args.command == "release":
        release = client.get_release(args.id)
        print(f"Title: {release.title}")
        print(f"Artists: {', '.join([a.name for a in release.artists])}")
        print(f"Labels: {', '.join([l.name for l in release.labels])}")
        print(f"Year: {release.year}")
        print(f"Genres: {', '.join(release.genres)}")
        print(f"Styles: {', '.join(release.styles)}")
        print("Tracklist:")
        for track in release.tracklist:
            print(f"- {track.position}. {track.title} ({track.duration})")
            if track.artists:
                print(f"  Artists: {', '.join([a.name for a in track.artists])}")
            if track.extraartists:
                print(
                    f"  Extra Artists: {', '.join([f'{a.name} ({a.role})' for a in track.extraartists])}",
                )
            print()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
