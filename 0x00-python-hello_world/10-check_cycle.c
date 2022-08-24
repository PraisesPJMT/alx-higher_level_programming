#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: Singly-linked list.
 *
 * Return: (0) If there is no cycle
 *         (-1) If there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *previous, *current;

	if (list == NULL || list->next == NULL)
		return (0);

	previous = list->next;
	current = list->next->next;

	while (previous && current && current->next)
	{
		if (previous == current)
			return (1);

		previous = previous->next;
		current = current->next->next;
	}

	return (0);
}