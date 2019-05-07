#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 1 if true, 0 if false
 */
int is_palindrome(listint_t **head)
{
	static int arr[50];
	int i = 0, j = 0;
	listint_t *current = *head;

	if (!*head)
		return (1);
	while (current)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	i--;
	while (j <= i)
	{
		if (arr[j] != arr[i])
			return (0);
		j++;
		i--;
	}
	return (1);

}
/*
	register int i, len;
	listint_t *start, *end;

	if (!*head)
		return (1);
	i = 0;
	len = listint_len(*head) - 1;

	while (i < len)
	{
		start = get_nodeint_at_index(*head, i);
		end = get_nodeint_at_index(*head, len);
		if (start->n != end->n)
			return (0);
		i++;
		len--;
	}
	return (1);
*/
/**
 * listint_len - returns the number of elements in a
 * linked listint_t list
 * @h: pointer to head of list
 * Return: number of elements
 */
size_t listint_len(const listint_t *h)
{
	register size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}

/**
 * get_nodeint_at_index - returns the nth node of a listint_t linked list
 * @head: pointer to head of list
 * @index: index of value to be returned
 * Return: address of node at input index
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current;

	register uint count = 0;

	current = head;
	while (current)
	{
		if (count == index)
			return (current);
		count++;
		current = current->next;
	}
	return (current);
}
