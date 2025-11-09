import pytest
from contextlib import nullcontext
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.heap_sort import heap_sort


class TestSort:
    @pytest.mark.parametrize(
        "arr, res, expectations",
        [
            ([3, 2, 4, 1, 5], [1, 2, 3, 4, 5], nullcontext()),
            # Для теста с TypeError лучше разделить на отдельные тесты
        ]
    )
    def test_sort_normal_cases(self, arr, res, expectations):
        with expectations:
            assert heap_sort(arr.copy()) == res
            assert quick_sort(arr.copy()) == res
            assert insertion_sort(arr.copy()) == res
            assert bubble_sort(arr.copy()) == res
    
    def test_sort_with_mixed_types_raises_error(self):
        """Тестируем поведение при смешанных типах"""
        arr = [1, 6, "t", 7, 3]
        
        # Разные алгоритмы могут по-разному обрабатывать TypeError
        # Лучше тестировать каждый отдельно
        with pytest.raises((TypeError, Exception)):
            heap_sort(arr.copy())
        
        with pytest.raises((TypeError, Exception)):
            quick_sort(arr.copy())
        
        with pytest.raises((TypeError, Exception)):
            insertion_sort(arr.copy())
        
        with pytest.raises((TypeError, Exception)):
            bubble_sort(arr.copy())


class TestEdgeCases:
    @pytest.mark.parametrize(
        "edge_arr, edge_res",
        [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([4, 4, 4, 4], [4, 4, 4, 4]),
            ([1, 7, 2, 6, 3, 5, 4], [1, 2, 3, 4, 5, 6, 7]),
            ([4, 1, 5, 2, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7]),
            ([-1, -2, 0, -5, -8, -3], [-8, -5, -3, -2, -1, 0]),
            ([1, 0.5, 0.6, 0.3, 2], [0.3, 0.5, 0.6, 1, 2]),
        ]
    )
    def test_boundary_cases(self, edge_arr, edge_res):
        # Используем copy() чтобы избежать изменения исходных данных
        assert heap_sort(edge_arr.copy()) == edge_res
        assert quick_sort(edge_arr.copy()) == edge_res
        assert insertion_sort(edge_arr.copy()) == edge_res
        assert bubble_sort(edge_arr.copy()) == edge_res
    
    def test_special_floats(self):
        """Отдельный тест для специальных float значений"""
        arr = [float('inf'), -float('inf'), 1e100, -1e100]
        expected = [-float('inf'), -1e100, 1e100, float('inf')]
        
        assert heap_sort(arr.copy()) == expected
        assert quick_sort(arr.copy()) == expected
        assert insertion_sort(arr.copy()) == expected
        assert bubble_sort(arr.copy()) == expected


class TestIndividualSorts:
    """Тесты для специфического поведения каждого алгоритма"""
    
    def test_heap_sort_specific(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert heap_sort(arr) == sorted(arr)
    
    def test_quick_sort_specific(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert quick_sort(arr) == sorted(arr)
    
    def test_insertion_sort_specific(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert insertion_sort(arr) == sorted(arr)
    
    def test_bubble_sort_specific(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert bubble_sort(arr) == sorted(arr)
