# https://www.codewars.com/kata/52996b5c99fdcb5f20000004/
from collections import Counter


def runoff(voters):
    """
    Your task is to implement a function that calculates an election winner from a list of voter selections using an
    Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this
    kata):

    - Each voter selects several candidates in order of preference.
    - The votes are tallied from each voter's first choice.
    - If the first-place candidate has more than half the total votes, they win.
    - Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
    - In case of a tie for least, remove all of the tying candidates.
    - In case of a complete tie between every candidate, return None.
    - Start over.
    - Continue until somebody has more than half the votes; they are the winner.

    Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in
    descending order of preference. You should return the symbol corresponding to the winning candidate. See the
    default test for an example!

    >>> runoff([["dem", "ind", "rep"], ["rep", "ind", "dem"], ["ind", "dem", "rep"], ["ind", "rep", "dem"]])
    'ind'

    >>> runoff([["a", "c", "d", "e", "b"], ["e", "b", "d", "c", "a"], ["d", "e", "c", "a", "b"],\
                ["c", "e", "d", "b", "a"], ["b", "e", "a", "c", "d"]])
    'None'

    >>> runoff([['Daisuke Aramaki', 'Gihren Zabi', 'Lex Luthor', 'Drake Luft', 'Abelt Dessler'],\
                ['Abelt Dessler', 'Drake Luft', 'Daisuke Aramaki', 'Lex Luthor', 'Gihren Zabi'],\
                ['Lex Luthor', 'Gihren Zabi', 'Daisuke Aramaki', 'Drake Luft', 'Abelt Dessler']])
    'None'
    """

    while len(voters) > 0 and len(voters[0]) > 0:
        # Tally votes from each voter's first choice, including those that did not get any votes
        results = dict(Counter(vote[0] for vote in voters))
        [results.setdefault(cand, 0) for cand in voters[0]]

        for cand in voters[0]:
                results.setdefault(cand, 0)

        # If a candidate has more than half the total votes, they win.
        winner = next((cand for cand, votes in results.items() if votes > len(voters) / 2), None)
        if winner is not None:
                return winner

        # Otherwise, find the candidate(s) who got the least votes and remove them from each person's voting list.
        least_votes = min((results.values()))
        removed_candidates = [cand for cand, votes in results.items() if votes == least_votes]
        voters = [[cand for cand in vote if cand not in removed_candidates] for vote in voters]

    # The list of potential candidates is empty after elimination. No winner could be identified
    return 'None'
